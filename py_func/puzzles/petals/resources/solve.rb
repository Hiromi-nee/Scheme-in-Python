puts "Solving"
require 'pty'

PTY.spawn('./petals.elf32') do |output, input, pid|
  while true do
	buffer=""
	answer=0
	output.readpartial(1024,buffer) until buffer =~ /Your answer:/ or buffer =~ /Very good!/
		buffer.split("\n").each do |line|
			puts line
			if line.match(/       \d          \d          \d          \d          \d          \d/)
				line.scan(/\d/).each do |num|
					answer+=4 if num =~ /5/
					answer+=2 if num =~/3/
				end
			end
		end
	input.write("#{answer}"+"\n")
  end
end
