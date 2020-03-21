# Terraform::AzureRM::KeyVaultCertificate CertificatePolicy LifetimeAction Action

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actiontype" title="ActionType">ActionType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#actiontype" title="ActionType">ActionType</a>: <i>String</i>
</pre>

## Properties

#### ActionType

The Type of action to be performed when the lifetime trigger is triggerec. Possible values include `AutoRenew` and `EmailContacts`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

