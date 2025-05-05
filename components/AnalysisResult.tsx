import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

interface AnalysisResultProps {
  result: string
}

export default function AnalysisResult({ result }: AnalysisResultProps) {
  return (
    <Card className="mt-8 max-w-md">
      <CardHeader>
        <CardTitle>Analysis Result</CardTitle>
      </CardHeader>
      <CardContent>
        <p>{result}</p>
      </CardContent>
    </Card>
  )
}

