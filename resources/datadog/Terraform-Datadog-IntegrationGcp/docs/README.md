# Terraform::Datadog::IntegrationGcp

Provides a Datadog - Google Cloud Platform integration resource. This can be used to create and manage Datadog - Google Cloud Platform integration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::IntegrationGcp",
    "Properties" : {
        "<a href="#clientemail" title="ClientEmail">ClientEmail</a>" : <i>String</i>,
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#hostfilters" title="HostFilters">HostFilters</a>" : <i>String</i>,
        "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>,
        "<a href="#privatekeyid" title="PrivateKeyId">PrivateKeyId</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::IntegrationGcp
Properties:
    <a href="#clientemail" title="ClientEmail">ClientEmail</a>: <i>String</i>
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#hostfilters" title="HostFilters">HostFilters</a>: <i>String</i>
    <a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
    <a href="#privatekeyid" title="PrivateKeyId">PrivateKeyId</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
</pre>

## Properties

#### ClientEmail

Your email found in your JSON service account key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

Your ID found in your JSON service account key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostFilters

Limit the GCE instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

Your private key name found in your JSON service account key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKeyId

Your private key ID found in your JSON service account key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

Your Google Cloud project ID found in your JSON service account key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

