# TF::Dynatrace::RequestAttribute DataSourcesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#capturingandstoragelocation" title="CapturingAndStorageLocation">CapturingAndStorageLocation</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#iibnodetype" title="IibNodeType">IibNodeType</a>" : <i>String</i>,
    "<a href="#parametername" title="ParameterName">ParameterName</a>" : <i>String</i>,
    "<a href="#sessionattributetechnology" title="SessionAttributeTechnology">SessionAttributeTechnology</a>" : <i>String</i>,
    "<a href="#source" title="Source">Source</a>" : <i>String</i>,
    "<a href="#technology" title="Technology">Technology</a>" : <i>String</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#cicssdkmethodnodecondition" title="CicsSdkMethodNodeCondition">CicsSdkMethodNodeCondition</a>" : <i>[ <a href="cicssdkmethodnodeconditiondefinition.md">CicsSdkMethodNodeConditionDefinition</a>, ... ]</i>,
    "<a href="#iiblabelmethodnodecondition" title="IibLabelMethodNodeCondition">IibLabelMethodNodeCondition</a>" : <i>[ <a href="iiblabelmethodnodeconditiondefinition.md">IibLabelMethodNodeConditionDefinition</a>, ... ]</i>,
    "<a href="#iibmethodnodecondition" title="IibMethodNodeCondition">IibMethodNodeCondition</a>" : <i>[ <a href="iibmethodnodeconditiondefinition.md">IibMethodNodeConditionDefinition</a>, ... ]</i>,
    "<a href="#methods" title="Methods">Methods</a>" : <i>[ <a href="methodsdefinition.md">MethodsDefinition</a>, ... ]</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>[ <a href="scopedefinition.md">ScopeDefinition</a>, ... ]</i>,
    "<a href="#valueprocessing" title="ValueProcessing">ValueProcessing</a>" : <i>[ <a href="valueprocessingdefinition.md">ValueProcessingDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#capturingandstoragelocation" title="CapturingAndStorageLocation">CapturingAndStorageLocation</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#iibnodetype" title="IibNodeType">IibNodeType</a>: <i>String</i>
<a href="#parametername" title="ParameterName">ParameterName</a>: <i>String</i>
<a href="#sessionattributetechnology" title="SessionAttributeTechnology">SessionAttributeTechnology</a>: <i>String</i>
<a href="#source" title="Source">Source</a>: <i>String</i>
<a href="#technology" title="Technology">Technology</a>: <i>String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#cicssdkmethodnodecondition" title="CicsSdkMethodNodeCondition">CicsSdkMethodNodeCondition</a>: <i>
      - <a href="cicssdkmethodnodeconditiondefinition.md">CicsSdkMethodNodeConditionDefinition</a></i>
<a href="#iiblabelmethodnodecondition" title="IibLabelMethodNodeCondition">IibLabelMethodNodeCondition</a>: <i>
      - <a href="iiblabelmethodnodeconditiondefinition.md">IibLabelMethodNodeConditionDefinition</a></i>
<a href="#iibmethodnodecondition" title="IibMethodNodeCondition">IibMethodNodeCondition</a>: <i>
      - <a href="iibmethodnodeconditiondefinition.md">IibMethodNodeConditionDefinition</a></i>
<a href="#methods" title="Methods">Methods</a>: <i>
      - <a href="methodsdefinition.md">MethodsDefinition</a></i>
<a href="#scope" title="Scope">Scope</a>: <i>
      - <a href="scopedefinition.md">ScopeDefinition</a></i>
<a href="#valueprocessing" title="ValueProcessing">ValueProcessing</a>: <i>
      - <a href="valueprocessingdefinition.md">ValueProcessingDefinition</a></i>
</pre>

## Properties

#### CapturingAndStorageLocation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IibNodeType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParameterName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAttributeTechnology

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Technology

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CicsSdkMethodNodeCondition

_Required_: No

_Type_: List of <a href="cicssdkmethodnodeconditiondefinition.md">CicsSdkMethodNodeConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IibLabelMethodNodeCondition

_Required_: No

_Type_: List of <a href="iiblabelmethodnodeconditiondefinition.md">IibLabelMethodNodeConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IibMethodNodeCondition

_Required_: No

_Type_: List of <a href="iibmethodnodeconditiondefinition.md">IibMethodNodeConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Methods

_Required_: No

_Type_: List of <a href="methodsdefinition.md">MethodsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: List of <a href="scopedefinition.md">ScopeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueProcessing

_Required_: No

_Type_: List of <a href="valueprocessingdefinition.md">ValueProcessingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

