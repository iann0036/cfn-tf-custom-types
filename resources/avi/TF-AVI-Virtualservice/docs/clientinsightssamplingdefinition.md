# TF::AVI::Virtualservice ClientInsightsSamplingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientip" title="ClientIp">ClientIp</a>" : <i>[ <a href="clientipdefinition.md">ClientIpDefinition</a>, ... ]</i>,
    "<a href="#sampleuris" title="SampleUris">SampleUris</a>" : <i>[ <a href="sampleurisdefinition.md">SampleUrisDefinition</a>, ... ]</i>,
    "<a href="#skipuris" title="SkipUris">SkipUris</a>" : <i>[ <a href="skipurisdefinition.md">SkipUrisDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clientip" title="ClientIp">ClientIp</a>: <i>
      - <a href="clientipdefinition.md">ClientIpDefinition</a></i>
<a href="#sampleuris" title="SampleUris">SampleUris</a>: <i>
      - <a href="sampleurisdefinition.md">SampleUrisDefinition</a></i>
<a href="#skipuris" title="SkipUris">SkipUris</a>: <i>
      - <a href="skipurisdefinition.md">SkipUrisDefinition</a></i>
</pre>

## Properties

#### ClientIp

_Required_: No

_Type_: List of <a href="clientipdefinition.md">ClientIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleUris

_Required_: No

_Type_: List of <a href="sampleurisdefinition.md">SampleUrisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipUris

_Required_: No

_Type_: List of <a href="skipurisdefinition.md">SkipUrisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

