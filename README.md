Docker image for Blockland servers
==================================

This is an attempt for creating a standard environment for Blockland servers on Linux using Docker.

Since getting Blockland to run flawlessly under Linux is a notoriously finicky process that nobody really understands, it's better to get it done with once in a reproducible manner.

Usage
-----

[Install Docker](https://www.docker.io/gettingstarted/), then run (remember sudo if you're not already root)

    # docker run -i -t -P teozkr/blockland

This should create and start the Blockland instance, as well as give you access to it's console.

Updating
--------

    # docker pull teozkr/blockland

Building it yourself
--------------------

Clone the repo, then run (from the repo directory)

    # docker build -t blockland .

Then remember to run `blockland` instead of `teozkr/blockland`. You can also use any other name instead if you please, as long as you're consistent.

FAQ
===

How do I run on another port?
-----------------------------

Add `-port 29000` to the end of the command in order to launch on the port 29000.

Why aren't my settings or add-ons saved?
----------------------------------------

They can be! Just add `-v add-ons:/opt/blockland/Add-Ons -v config:/opt/blockland/config` to the command, right after `-P`, in order to save add-ons and config in the add-ons and config subfolders of the current folder, respectively.

Why do I have to re-enter my key every time I restart the server?
-----------------------------------------------------------------

This happens because Blockland uses the identity of the network card in it's encryption of the key, while Docker recreates the fake card on every container creation, invalidating the encrypted key.
Currently investigating solutions, but none would be elegant without the cooperation of at least one of these parties.

I don't like docker!
--------------------

Even if you don't like Docker itself, this should hopefully produce a Dockerfile which can be used as a rough template for creating servers manually.

You're an idiot, why would you run Blockland as root!
-----------------------------------------------------

It only has privileges inside the Docker container, which is recreated for every restart anyway. Setting up more users when it's already isolated just isn't worth the effort.

