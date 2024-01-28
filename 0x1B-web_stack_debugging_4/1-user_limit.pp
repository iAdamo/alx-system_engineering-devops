# Increase max number of file descriptors for holberton user

exec { 'hard_file_descriptors':
        provider => shell,
        command  => 'sed -i "/^holberton hard nofile/s/5/50/g" /etc/security/limits.conf',
}
exec { 'soft_file_descriptors':
        provider => shell,
        command  => 'sed -i "/^holberton soft nofile/s/4/40/g" /etc/security/limits.conf',
}
