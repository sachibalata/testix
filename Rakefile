require 'yaml'

task :examples do
    sh "python -m pytest -sv examples/tests/test_*.py"
end

task :units do
    sh "python -m pytest -sv test/"
end

task :all_tests_included do
  tests = YAML.load_file '.github/workflows/tests.yaml'
  check_names = tests["jobs"].keys.filter {|job| job != 'All-OK'}
  all_ok_needs = tests['jobs']['All-OK']['needs']
  missing = Set.new(check_names) - Set.new(all_ok_needs)
  impossible = Set.new(all_ok_needs) - Set.new(check_names)
  fail("All-OK missing some tests: #{missing.to_a}") if missing.size > 0
  fail("All-OK demanding non existent jobs: #{impossible.to_a}") if impossible.size > 0
end
