"use client"

import type React from "react"

import { useState, useRef } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent } from "@/components/ui/card"
import { useToast } from "@/components/ui/use-toast"

export function AudioUpload() {
  const [audioFile, setAudioFile] = useState<File | null>(null)
  const [isAnalyzing, setIsAnalyzing] = useState(false)
  const [analysisResult, setAnalysisResult] = useState<string | null>(null)
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const { toast } = useToast()

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (file) {
      setAudioFile(file)
      setAnalysisResult(null)
      visualizeAudio(file)
    }
  }

  const visualizeAudio = async (file: File) => {
    const audioContext = new (window.AudioContext || (window as any).webkitAudioContext)()
    const analyser = audioContext.createAnalyser()
    const source = audioContext.createBufferSource()

    const arrayBuffer = await file.arrayBuffer()
    const audioBuffer = await audioContext.decodeAudioData(arrayBuffer)

    source.buffer = audioBuffer
    source.connect(analyser)
    analyser.connect(audioContext.destination)

    const canvas = canvasRef.current
    if (!canvas) return

    const canvasCtx = canvas.getContext("2d")
    if (!canvasCtx) return

    const bufferLength = analyser.frequencyBinCount
    const dataArray = new Uint8Array(bufferLength)

    const draw = () => {
      requestAnimationFrame(draw)
      analyser.getByteFrequencyData(dataArray)

      canvasCtx.fillStyle = "rgb(200, 200, 200)"
      canvasCtx.fillRect(0, 0, canvas.width, canvas.height)

      const barWidth = (canvas.width / bufferLength) * 2.5
      let barHeight
      let x = 0

      for (let i = 0; i < bufferLength; i++) {
        barHeight = dataArray[i] / 2
        canvasCtx.fillStyle = `rgb(${barHeight + 100}, 50, 50)`
        canvasCtx.fillRect(x, canvas.height - barHeight / 2, barWidth, barHeight)
        x += barWidth + 1
      }
    }

    source.start(0)
    draw()
  }

  const analyzeBabyCry = async () => {
    if (!audioFile) return

    setIsAnalyzing(true)
    // Simulating analysis with a delay
    await new Promise((resolve) => setTimeout(resolve, 2000))

    const reasons = ["hunger", "tiredness", "discomfort", "colic", "seeking attention"]
    const result = `Based on the analysis, the baby is likely experiencing ${reasons[Math.floor(Math.random() * reasons.length)]}.`
    setAnalysisResult(result)
    setIsAnalyzing(false)

    toast({
      title: "Analysis Complete",
      description: "The baby cry has been analyzed successfully.",
    })
  }

  return (
    <div className="space-y-4">
      <Input type="file" accept="audio/*" onChange={handleFileChange} />
      {audioFile && (
        <Card>
          <CardContent className="p-4">
            <canvas ref={canvasRef} width="300" height="100" />
          </CardContent>
        </Card>
      )}
      <Button onClick={analyzeBabyCry} disabled={!audioFile || isAnalyzing}>
        {isAnalyzing ? "Analyzing..." : "Analyze Baby Cry"}
      </Button>
      {analysisResult && (
        <Card>
          <CardContent className="p-4">
            <p className="font-semibold">Analysis Result:</p>
            <p>{analysisResult}</p>
          </CardContent>
        </Card>
      )}
    </div>
  )
}

