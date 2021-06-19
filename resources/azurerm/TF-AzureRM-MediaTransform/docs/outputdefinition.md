# TF::AzureRM::MediaTransform OutputDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#onerroraction" title="OnErrorAction">OnErrorAction</a>" : <i>String</i>,
    "<a href="#relativepriority" title="RelativePriority">RelativePriority</a>" : <i>String</i>,
    "<a href="#audioanalyzerpreset" title="AudioAnalyzerPreset">AudioAnalyzerPreset</a>" : <i>[ <a href="audioanalyzerpresetdefinition.md">AudioAnalyzerPresetDefinition</a>, ... ]</i>,
    "<a href="#builtinpreset" title="BuiltinPreset">BuiltinPreset</a>" : <i>[ <a href="builtinpresetdefinition.md">BuiltinPresetDefinition</a>, ... ]</i>,
    "<a href="#facedetectorpreset" title="FaceDetectorPreset">FaceDetectorPreset</a>" : <i>[ <a href="facedetectorpresetdefinition.md">FaceDetectorPresetDefinition</a>, ... ]</i>,
    "<a href="#videoanalyzerpreset" title="VideoAnalyzerPreset">VideoAnalyzerPreset</a>" : <i>[ <a href="videoanalyzerpresetdefinition.md">VideoAnalyzerPresetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#onerroraction" title="OnErrorAction">OnErrorAction</a>: <i>String</i>
<a href="#relativepriority" title="RelativePriority">RelativePriority</a>: <i>String</i>
<a href="#audioanalyzerpreset" title="AudioAnalyzerPreset">AudioAnalyzerPreset</a>: <i>
      - <a href="audioanalyzerpresetdefinition.md">AudioAnalyzerPresetDefinition</a></i>
<a href="#builtinpreset" title="BuiltinPreset">BuiltinPreset</a>: <i>
      - <a href="builtinpresetdefinition.md">BuiltinPresetDefinition</a></i>
<a href="#facedetectorpreset" title="FaceDetectorPreset">FaceDetectorPreset</a>: <i>
      - <a href="facedetectorpresetdefinition.md">FaceDetectorPresetDefinition</a></i>
<a href="#videoanalyzerpreset" title="VideoAnalyzerPreset">VideoAnalyzerPreset</a>: <i>
      - <a href="videoanalyzerpresetdefinition.md">VideoAnalyzerPresetDefinition</a></i>
</pre>

## Properties

#### OnErrorAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelativePriority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AudioAnalyzerPreset

_Required_: No

_Type_: List of <a href="audioanalyzerpresetdefinition.md">AudioAnalyzerPresetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuiltinPreset

_Required_: No

_Type_: List of <a href="builtinpresetdefinition.md">BuiltinPresetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaceDetectorPreset

_Required_: No

_Type_: List of <a href="facedetectorpresetdefinition.md">FaceDetectorPresetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VideoAnalyzerPreset

_Required_: No

_Type_: List of <a href="videoanalyzerpresetdefinition.md">VideoAnalyzerPresetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

