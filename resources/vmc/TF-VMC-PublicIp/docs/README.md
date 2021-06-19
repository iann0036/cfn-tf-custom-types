# TF::VMC::PublicIp

Provides a resource to manage public IPs.
~> **Note:** Public IP resource implicitly depends on SDDC resource creation. SDDC must be provisioned before a public IP can be created. For details on how to provision a SDDC refer to [vmc_sddc](https://www.terraform.io/docs/providers/vmc/r/sddc.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VMC::PublicIp",
    "Properties" : {
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#nsxtreverseproxyurl" title="NsxtReverseProxyUrl">NsxtReverseProxyUrl</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VMC::PublicIp
Properties:
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#nsxtreverseproxyurl" title="NsxtReverseProxyUrl">NsxtReverseProxyUrl</a>: <i>String</i>
</pre>

## Properties

#### DisplayName

Display name for public IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxtReverseProxyUrl

NSXT reverse proxy url for managing public IP. Computed after SDDC creation.

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

#### Id

Returns the <code>Id</code> value.

#### Ip

Returns the <code>Ip</code> value.

