# TF::AWS::WafregionalWebAcl LoggingConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#logdestination" title="LogDestination">LogDestination</a>" : <i>String</i>,
    "<a href="#redactedfields" title="RedactedFields">RedactedFields</a>" : <i>[ <a href="redactedfieldsdefinition.md">RedactedFieldsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#logdestination" title="LogDestination">LogDestination</a>: <i>String</i>
<a href="#redactedfields" title="RedactedFields">RedactedFields</a>: <i>
      - <a href="redactedfieldsdefinition.md">RedactedFieldsDefinition</a></i>
</pre>

## Properties

#### LogDestination

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedactedFields

_Required_: No

_Type_: List of <a href="redactedfieldsdefinition.md">RedactedFieldsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

