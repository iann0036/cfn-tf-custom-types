# TF::AzureDevOps::ServiceendpointAzurerm CredentialsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#serviceprincipalid" title="Serviceprincipalid">Serviceprincipalid</a>" : <i>String</i>,
    "<a href="#serviceprincipalkey" title="Serviceprincipalkey">Serviceprincipalkey</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#serviceprincipalid" title="Serviceprincipalid">Serviceprincipalid</a>: <i>String</i>
<a href="#serviceprincipalkey" title="Serviceprincipalkey">Serviceprincipalkey</a>: <i>String</i>
</pre>

## Properties

#### Serviceprincipalid

The service principal application Id
- `serviceprincipalkey` - (Required) The service principal secret.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Serviceprincipalkey

The service principal secret.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

