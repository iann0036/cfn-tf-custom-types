# TF::TencentCloud::ApiGatewayService

Use this resource to create API gateway service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ApiGatewayService",
    "Properties" : {
        "<a href="#exclusivesetname" title="ExclusiveSetName">ExclusiveSetName</a>" : <i>String</i>,
        "<a href="#ipversion" title="IpVersion">IpVersion</a>" : <i>String</i>,
        "<a href="#nettype" title="NetType">NetType</a>" : <i>[ String, ... ]</i>,
        "<a href="#prelimit" title="PreLimit">PreLimit</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#releaselimit" title="ReleaseLimit">ReleaseLimit</a>" : <i>Double</i>,
        "<a href="#servicedesc" title="ServiceDesc">ServiceDesc</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
        "<a href="#testlimit" title="TestLimit">TestLimit</a>" : <i>Double</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ApiGatewayService
Properties:
    <a href="#exclusivesetname" title="ExclusiveSetName">ExclusiveSetName</a>: <i>String</i>
    <a href="#ipversion" title="IpVersion">IpVersion</a>: <i>String</i>
    <a href="#nettype" title="NetType">NetType</a>: <i>
      - String</i>
    <a href="#prelimit" title="PreLimit">PreLimit</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#releaselimit" title="ReleaseLimit">ReleaseLimit</a>: <i>Double</i>
    <a href="#servicedesc" title="ServiceDesc">ServiceDesc</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
    <a href="#testlimit" title="TestLimit">TestLimit</a>: <i>Double</i>
</pre>

## Properties

#### ExclusiveSetName

Self-deployed cluster name, which is used to specify the self-deployed cluster where the service is to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpVersion

IP version number. Valid values: `IPv4`, `IPv6`. Default value: `IPv4`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetType

Network type list, which is used to specify the supported network types. Valid values: `INNER`, `OUTER`. `INNER` indicates access over private network, and `OUTER` indicates access over public network.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreLimit

API QPS value. Enter a positive number to limit the API query rate per second `QPS`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Service frontend request type. Valid values: `http`, `https`, `http&https`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReleaseLimit

API QPS value. Enter a positive number to limit the API query rate per second `QPS`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDesc

Custom service description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

Custom service name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestLimit

API QPS value. Enter a positive number to limit the API query rate per second `QPS`.

_Required_: No

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

#### ApiList

Returns the <code>ApiList</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### InnerHttpPort

Returns the <code>InnerHttpPort</code> value.

#### InnerHttpsPort

Returns the <code>InnerHttpsPort</code> value.

#### InternalSubDomain

Returns the <code>InternalSubDomain</code> value.

#### ModifyTime

Returns the <code>ModifyTime</code> value.

#### OuterSubDomain

Returns the <code>OuterSubDomain</code> value.

#### UsagePlanList

Returns the <code>UsagePlanList</code> value.

