# Terraform::AzureRM::PrivateDnsMxRecord Record

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

The FQDN of the exchange to MX record points to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preference

The preference of the MX record.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

