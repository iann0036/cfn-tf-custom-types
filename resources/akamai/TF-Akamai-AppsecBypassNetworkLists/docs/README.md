# TF::Akamai::AppsecBypassNetworkLists

Use the `akamai_appsec_bypass_network_lists` resource to update which network lists to use in the
bypass network lists settings. Note: this resource is only applicable to WAP (Web Application
Protector) configurations.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::AppsecBypassNetworkLists",
    "Properties" : {
        "<a href="#bypassnetworklist" title="BypassNetworkList">BypassNetworkList</a>" : <i>[ String, ... ]</i>,
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>Double</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::AppsecBypassNetworkLists
Properties:
    <a href="#bypassnetworklist" title="BypassNetworkList">BypassNetworkList</a>: <i>
      - String</i>
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>Double</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
</pre>

## Properties

#### BypassNetworkList

A list containing the IDs of the network lists to use.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigId

The configuration ID to use.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The version number of the configuration to use.

_Required_: Yes

_Type_: Double

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

