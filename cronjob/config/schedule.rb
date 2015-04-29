require "date"

every 1.minutes do
  command "touch /var/tmp/sentinel" if Date.today.sunday? || Date.today.saturday?
end

every 2.minutes do
  command "touch /var/tmp/sentinel" unless Date.today.sunday? && Date.today.saturday?
end