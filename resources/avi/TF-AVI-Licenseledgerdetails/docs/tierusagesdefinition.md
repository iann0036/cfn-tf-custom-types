# TF::AVI::Licenseledgerdetails TierUsagesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#tier" title="Tier">Tier</a>" : <i>String</i>,
    "<a href="#usage" title="Usage">Usage</a>" : <i>[ <a href="usagedefinition.md">UsageDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#tier" title="Tier">Tier</a>: <i>String</i>
<a href="#usage" title="Usage">Usage</a>: <i>
      - <a href="usagedefinition.md">UsageDefinition</a></i>
</pre>

## Properties

#### Tier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Usage

_Required_: No

_Type_: List of <a href="usagedefinition.md">UsageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

