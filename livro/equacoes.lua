-- Numera as equações em destaque: $$...$$ vira \begin{equation}...\end{equation}.
function Math(el)
  if el.mathtype == "DisplayMath" then
    local t = el.text
    if t:find("\\tag") or t:find("\\begin{align") or t:find("\\begin{equation") or t:find("\\begin{gather") then
      return pandoc.RawInline("latex", "\\[" .. t .. "\\]")
    end
    return pandoc.RawInline("latex", "\\begin{equation}" .. t .. "\\end{equation}")
  end
end
