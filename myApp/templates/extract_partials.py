import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract comparison marquee
m = re.search(r'(<!-- ===== SECTION 5: PREMIUM COMPARISON MARQUEE.*?</section>)', content, re.DOTALL)
if m:
    with open('partials/comparison-marquee.html', 'w', encoding='utf-8') as f:
        f.write(m.group(1))

# Extract programs
m = re.search(r'(<!-- ===== SECTION 6: SERVICES.*?</section>)', content, re.DOTALL)
if m:
    with open('partials/programs.html', 'w', encoding='utf-8') as f:
        f.write(m.group(1))

# Extract about
m = re.search(r'(<!-- ===== SECTION 7: ABOUT DR. GLEN.*?</section>)', content, re.DOTALL)
if m:
    with open('partials/about.html', 'w', encoding='utf-8') as f:
        f.write(m.group(1))

# Extract lead magnet
m = re.search(r'(<!-- ===== SECTION 8: LEAD MAGNET.*?</section>)', content, re.DOTALL)
if m:
    with open('partials/lead-magnet.html', 'w', encoding='utf-8') as f:
        f.write(m.group(1))

# Extract final CTA
m = re.search(r'(<!-- ===== SECTION 9: FINAL CTA.*?</section>)', content, re.DOTALL)
if m:
    with open('partials/final-cta.html', 'w', encoding='utf-8') as f:
        f.write(m.group(1))

# Extract footer
m = re.search(r'(<!-- ===== FOOTER =====.*?</footer>)', content, re.DOTALL)
if m:
    with open('partials/footer.html', 'w', encoding='utf-8') as f:
        f.write(m.group(1))

# Extract scripts (from first script tag to end of body/html)
m = re.search(r'(<script>.*?</script>\s*<!-- Bottom-right.*?</script>\s*</body>\s*</html>)', content, re.DOTALL)
if m:
    with open('partials/scripts.html', 'w', encoding='utf-8') as f:
        f.write(m.group(1))

print("All partials extracted successfully!")

