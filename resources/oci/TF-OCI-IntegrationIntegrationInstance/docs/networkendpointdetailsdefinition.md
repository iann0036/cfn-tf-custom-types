# TF::OCI::IntegrationIntegrationInstance NetworkEndpointDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowlistedhttpips" title="AllowlistedHttpIps">AllowlistedHttpIps</a>" : <i>[ String, ... ]</i>,
    "<a href="#isintegrationvcnallowlisted" title="IsIntegrationVcnAllowlisted">IsIntegrationVcnAllowlisted</a>" : <i>Boolean</i>,
    "<a href="#networkendpointtype" title="NetworkEndpointType">NetworkEndpointType</a>" : <i>String</i>,
    "<a href="#allowlistedhttpvcns" title="AllowlistedHttpVcns">AllowlistedHttpVcns</a>" : <i>[ <a href="allowlistedhttpvcnsdefinition.md">AllowlistedHttpVcnsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowlistedhttpips" title="AllowlistedHttpIps">AllowlistedHttpIps</a>: <i>
      - String</i>
<a href="#isintegrationvcnallowlisted" title="IsIntegrationVcnAllowlisted">IsIntegrationVcnAllowlisted</a>: <i>Boolean</i>
<a href="#networkendpointtype" title="NetworkEndpointType">NetworkEndpointType</a>: <i>String</i>
<a href="#allowlistedhttpvcns" title="AllowlistedHttpVcns">AllowlistedHttpVcns</a>: <i>
      - <a href="allowlistedhttpvcnsdefinition.md">AllowlistedHttpVcnsDefinition</a></i>
</pre>

## Properties

#### AllowlistedHttpIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsIntegrationVcnAllowlisted

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkEndpointType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowlistedHttpVcns

_Required_: No

_Type_: List of <a href="allowlistedhttpvcnsdefinition.md">AllowlistedHttpVcnsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

