# Terraform::DNS::MxRecordSet Mx

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exchange" title="Exchange">Exchange</a>" : <i>String</i>,
    "<a href="#preference" title="Preference">Preference</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#exchange" title="Exchange">Exchange</a>: <i>String</i>
<a href="#preference" title="Preference">Preference</a>: <i>Double</i>
</pre>

## Properties

#### Exchange

The FQDN of the mail exchange, include the trailing dot.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preference

The preference for the record.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

