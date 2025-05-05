"use client"

import type React from "react"

import { useState } from "react"
import { Input } from "@/components/ui/input"

interface AudioUploadProps {
  onAnalysis: (result: string) => void
}

export default function AudioUpload({ onAnalysis }: AudioUploadProps) {
  const [isLoading, setIsLoading] = useState(false)

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (!file) return

    setIsLoading(true)

    // TODO: Implement actual audio analysis
    // For now, we'll use a mock analysis function
    await new Promise((resolve) => setTimeout(resolve, 2000)) // Simulate processing time
    const mockResult = analyzeBabyCry(file.name)

    setIsLoading(false)
    onAnalysis(mockResult)
  }

  return (
    <div className="flex flex-col items-center gap-4">
      <Input type="file" accept="audio/*" onChange={handleFileUpload} disabled={isLoading} className="max-w-xs" />
      {isLoading && <p className="text-sm text-gray-500">Analyzing audio...</p>}
    </div>
  )
}

// Mock analysis function
function analyzeBabyCry(fileName: string): string {
  const reasons = ["hunger", "tiredness", "discomfort", "colic", "seeking attention"]
  return `Based on the analysis of "${fileName}", the baby is likely experiencing ${reasons[Math.floor(Math.random() * reasons.length)]}.`
}

