# Terraform::AzureRM::KubernetesCluster ServicePrincipal

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
    "<a href="#clientsecret" title="ClientSecret">ClientSecret</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
<a href="#clientsecret" title="ClientSecret">ClientSecret</a>: <i>String</i>
</pre>

## Properties

#### ClientId

The Client ID for the Service Principal.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSecret

The Client Secret for the Service Principal.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

