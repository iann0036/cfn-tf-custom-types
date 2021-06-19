# TF::Google::CloudbuildTrigger OptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>" : <i>Double</i>,
    "<a href="#dynamicsubstitutions" title="DynamicSubstitutions">DynamicSubstitutions</a>" : <i>Boolean</i>,
    "<a href="#env" title="Env">Env</a>" : <i>[ String, ... ]</i>,
    "<a href="#logstreamingoption" title="LogStreamingOption">LogStreamingOption</a>" : <i>String</i>,
    "<a href="#logging" title="Logging">Logging</a>" : <i>String</i>,
    "<a href="#machinetype" title="MachineType">MachineType</a>" : <i>String</i>,
    "<a href="#requestedverifyoption" title="RequestedVerifyOption">RequestedVerifyOption</a>" : <i>String</i>,
    "<a href="#secretenv" title="SecretEnv">SecretEnv</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourceprovenancehash" title="SourceProvenanceHash">SourceProvenanceHash</a>" : <i>[ String, ... ]</i>,
    "<a href="#substitutionoption" title="SubstitutionOption">SubstitutionOption</a>" : <i>String</i>,
    "<a href="#workerpool" title="WorkerPool">WorkerPool</a>" : <i>String</i>,
    "<a href="#volumes" title="Volumes">Volumes</a>" : <i>[ <a href="volumesdefinition.md">VolumesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>: <i>Double</i>
<a href="#dynamicsubstitutions" title="DynamicSubstitutions">DynamicSubstitutions</a>: <i>Boolean</i>
<a href="#env" title="Env">Env</a>: <i>
      - String</i>
<a href="#logstreamingoption" title="LogStreamingOption">LogStreamingOption</a>: <i>String</i>
<a href="#logging" title="Logging">Logging</a>: <i>String</i>
<a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
<a href="#requestedverifyoption" title="RequestedVerifyOption">RequestedVerifyOption</a>: <i>String</i>
<a href="#secretenv" title="SecretEnv">SecretEnv</a>: <i>
      - String</i>
<a href="#sourceprovenancehash" title="SourceProvenanceHash">SourceProvenanceHash</a>: <i>
      - String</i>
<a href="#substitutionoption" title="SubstitutionOption">SubstitutionOption</a>: <i>String</i>
<a href="#workerpool" title="WorkerPool">WorkerPool</a>: <i>String</i>
<a href="#volumes" title="Volumes">Volumes</a>: <i>
      - <a href="volumesdefinition.md">VolumesDefinition</a></i>
</pre>

## Properties

#### DiskSizeGb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSubstitutions

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogStreamingOption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestedVerifyOption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretEnv

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceProvenanceHash

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubstitutionOption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerPool

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volumes

_Required_: No

_Type_: List of <a href="volumesdefinition.md">VolumesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

