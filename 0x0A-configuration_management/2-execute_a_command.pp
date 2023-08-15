# Kills a process named 'killmenow" using Puppet
exec { 'killmenow':
  command => 'usr/tmp/pkill killmenow'
}
