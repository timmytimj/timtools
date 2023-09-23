#!/usr/bin/env perl

use strict;
use warnings;

my $output = `defaults read`;

my $current_domain;
my %settings;

foreach my $line (split /\n/, $output) {
    chomp($line);

    if ($line =~ /^\s*$/) {
        # Skip empty lines
        next;
    } elsif ($line =~ /^\s*(\S+)\s*=\s*{/) {
        # Start of a new domain
        $current_domain = $1;
        $settings{$current_domain} = {};
    } elsif ($line =~ /^\s*(\S+)\s*=\s*\"([^\"]+)\";/) {
        # Key-value pair
        my $key = $1;
        my $value = $2;
        $settings{$current_domain}->{$key} = $value;
    }
}

# Print the parsed settings
foreach my $domain (keys %settings) {
    print "Domain: $domain\n";
    foreach my $key (keys %{$settings{$domain}}) {
        my $value = $settings{$domain}->{$key};
        print "  $key: $value\n";
    }
    print "\n";
}

