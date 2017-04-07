#!/usr/bin/perl
use Frontier::Client;
use Data::Dumper;
use REST::Client;
use JSON;
use MIME::Base64;

$ENV{HTTPS_CA_FILE} = "/data/scripts/sat6/katello-server-ca.crt";

=pod
print "Enter server: ";
chomp($host = <STDIN>);

print "Enter user: ";
chomp($user = <STDIN>);

system('stty -echo');
print "Enter Password: ";
chomp($pass = <STDIN>);
system('stty echo');
print "\n";
=cut
my $host = "prod.usersys.redhat.com";
my $user = "admin";
my $pass = "redhat";

my $ua = LWP::UserAgent->new();
$ua->agent('Mozilla');

my $fullserver = "https://" . $host;

my $client = REST::Client->new(host => $fullserver);
$client->addHeader('Content-Type', 'application/json');
$client->addHeader('charset', 'UTF-8');
$client->addHeader('Accept', 'application/json');

my $session = encode_base64("$user:$pass", '');


$client->GET('/api/hosts', {'Authorization' => "Basic $session", 'Accept' => 'application/json'});

#print "Response code: " . $client->responseCode() . "\n";

#print "Response: " . $client->responseContent() . "\n";

my $values = $client->responseContent();
print $values;

=podfor (@{$values})
{
  print "x\n";
  print $_->{'ip'} . "\n";
}


=pod
$client->setHost($fullserver);
$client->GET('/api/hosts', $headers);
if ($client->responseCode() eq '200')
{
    print "got /api/hosts\n";
}
else
{
    print "failed\n";
}

#my $response = from_json($client->responseContent());
#print Dumper($response);
=cut
