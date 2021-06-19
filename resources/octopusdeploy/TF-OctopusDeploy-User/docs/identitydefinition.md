# TF::OctopusDeploy::User IdentityDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#provider" title="Provider">Provider</a>" : <i>String</i>,
    "<a href="#claim" title="Claim">Claim</a>" : <i>[ <a href="claimdefinition.md">ClaimDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#provider" title="Provider">Provider</a>: <i>String</i>
<a href="#claim" title="Claim">Claim</a>: <i>
      - <a href="claimdefinition.md">ClaimDefinition</a></i>
</pre>

## Properties

#### Provider

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Claim

_Required_: No

_Type_: List of <a href="claimdefinition.md">ClaimDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

