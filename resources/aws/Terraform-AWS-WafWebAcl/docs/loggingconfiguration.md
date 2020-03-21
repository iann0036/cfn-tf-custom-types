# Terraform::AWS::WafWebAcl LoggingConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#logdestination" title="LogDestination">LogDestination</a>" : <i>String</i>,
    "<a href="#redactedfields" title="RedactedFields">RedactedFields</a>" : <i>[ &lt;a href=&#34;loggingconfiguration-redactedfields.md&#34;&gt;RedactedFields&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#logdestination" title="LogDestination">LogDestination</a>: <i>String</i>
<a href="#redactedfields" title="RedactedFields">RedactedFields</a>: <i>
      - &lt;a href=&#34;loggingconfiguration-redactedfields.md&#34;&gt;RedactedFields&lt;/a&gt;</i>
</pre>

## Properties

#### LogDestination

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedactedFields

_Required_: No
_Type_: List of &lt;a href=&#34;loggingconfiguration-redactedfields.md&#34;&gt;RedactedFields&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

