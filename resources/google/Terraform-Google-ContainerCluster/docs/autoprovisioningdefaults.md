# Terraform::Google::ContainerCluster AutoProvisioningDefaults

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#oauthscopes" title="OauthScopes">OauthScopes</a>" : <i>[ String, ... ]</i>,
    "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#oauthscopes" title="OauthScopes">OauthScopes</a>: <i>
      - String</i>
<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>String</i>
</pre>

## Properties

#### OauthScopes

Scopes that are used by NAP when creating node pools.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

The Google Cloud Platform Service Account to be used by the node VMs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

