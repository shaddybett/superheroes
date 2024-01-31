# puts "🦸‍♀️ Seeding powers..."
# Power.create([
#   { name: "super strength", description: "gives the wielder super-human strengths" },
#   { name: "flight", description: "gives the wielder the ability to fly through the skies at supersonic speed" },
#   { name: "super human senses", description: "allows the wielder to use her senses at a super-human level" },
#   { name: "elasticity", description: "can stretch the human body to extreme lengths" }
# ])

# puts "🦸‍♀️ Seeding heroes..."
# Hero.create([
#   { name: "Kamala Khan", super_name: "Ms. Marvel" },
#   { name: "Doreen Green", super_name: "Squirrel Girl" },
#   { name: "Gwen Stacy", super_name: "Spider-Gwen" },
#   { name: "Janet Van Dyne", super_name: "The Wasp" },
#   { name: "Wanda Maximoff", super_name: "Scarlet Witch" },
#   { name: "Carol Danvers", super_name: "Captain Marvel" },
#   { name: "Jean Grey", super_name: "Dark Phoenix" },
#   { name: "Ororo Munroe", super_name: "Storm" },
#   { name: "Kitty Pryde", super_name: "Shadowcat" },
#   { name: "Elektra Natchios", super_name: "Elektra" }
# ])

# puts "🦸‍♀️ Adding powers to heroes..."

# strengths = ["Strong", "Weak", "Average"]
# Hero.all.each do |hero|
#   rand(1..3).times do
#     # get a random power
#     power = Power.find(Power.pluck(:id).sample)

#     HeroPower.create!(hero_id: hero.id, power_id: power.id, strength: strengths.sample)
#   end
# end

# puts "🦸‍♀️ Done seeding!"




puts "🦸‍♀️ Seeding powers..."
powers_data = [
  { name: "super strength", description: "gives the wielder super-human strengths" },
  { name: "flight", description: "gives the wielder the ability to fly through the skies at supersonic speed" },
  { name: "super human senses", description: "allows the wielder to use her senses at a super-human level" },
  { name: "elasticity", description: "can stretch the human body to extreme lengths" }
]

powers_data.each do |power_attributes|
Power.create!(power_attributes)
 end

puts "🦸‍♀️ Seeding heroes..."
heroes_data = [
  { name: "Kamala Khan", super_name: "Ms. Marvel" },
  { name: "Doreen Green", super_name: "Squirrel Girl" },
  { name: "Gwen Stacy", super_name: "Spider-Gwen" },
  { name: "Janet Van Dyne", super_name: "The Wasp" },
  { name: "Wanda Maximoff", super_name: "Scarlet Witch" },
  { name: "Carol Danvers", super_name: "Captain Marvel" },
  { name: "Jean Grey", super_name: "Dark Phoenix" },
  { name: "Ororo Munroe", super_name: "Storm" },
  { name: "Kitty Pryde", super_name: "Shadowcat" },
  { name: "Elektra Natchios", super_name: "Elektra" }
]

heroes_data.each do |hero_attributes|
  Hero.create!(hero_attributes)
end

puts "🦸‍♀️ Adding powers to heroes..."

strengths = ["Strong", "Weak", "Average"]
Hero.all.each do |hero|
  rand(1..3).times do
    # get a random power
    power = Power.all.sample

    HeroPower.create!(hero: hero, power: power, strength: strengths.sample)
  end
end

puts "🦸‍♀️ Done seeding!"
