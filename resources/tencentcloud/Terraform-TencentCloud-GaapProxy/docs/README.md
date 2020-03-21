# Terraform::TencentCloud::GaapProxy

Provides a resource to create a GAAP proxy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::GaapProxy",
    "Properties" : {
        "<a href="#accessregion" title="AccessRegion">AccessRegion</a>" : <i>String</i>,
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>Double</i>,
        "<a href="#concurrent" title="Concurrent">Concurrent</a>" : <i>Double</i>,
        "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
        "<a href="#realserverregion" title="RealserverRegion">RealserverRegion</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::GaapProxy
Properties:
    <a href="#accessregion" title="AccessRegion">AccessRegion</a>: <i>String</i>
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>Double</i>
    <a href="#concurrent" title="Concurrent">Concurrent</a>: <i>Double</i>
    <a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
    <a href="#realserverregion" title="RealserverRegion">RealserverRegion</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### AccessRegion

Access region of the GAAP proxy, the available values include `NorthChina`, `EastChina`, `SouthChina`, `SouthwestChina`, `Hongkong`, `SL_TAIWAN`, `SoutheastAsia`, `Korea`, `SL_India`, `SL_Australia`, `Europe`, `SL_UK`, `SL_SouthAmerica`, `NorthAmerica`, `SL_MiddleUSA`, `Canada`, `SL_VIET`, `WestIndia`, `Thailand`, `Virginia`, `Russia`, `Japan` and `SL_Indonesia`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bandwidth

Maximum bandwidth of the GAAP proxy, unit is Mbps, the available values include `10`, `20`, `50`, `100`, `200`, `500` and `1000`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Concurrent

Maximum concurrency of the GAAP proxy, unit is 10k, the available values include `2`, `5`, `10`, `20`, `30`, `40`, `50`, `60`, `70`, `80`, `90` and `100`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

Indicates whether GAAP proxy is enabled, default value is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the GAAP proxy, the maximum length is 30.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

ID of the project within the GAAP proxy, '0' means is default project.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealserverRegion

Region of the GAAP realserver, the available values include `NorthChina`, `EastChina`, `SouthChina`, `SouthwestChina`, `Hongkong`, `SL_TAIWAN`, `SoutheastAsia`, `Korea`, `SL_India`, `SL_Australia`, `Europe`, `SL_UK`, `SL_SouthAmerica`, `NorthAmerica`, `SL_MiddleUSA`, `Canada`, `SL_VIET`, `WestIndia`, `Thailand`, `Virginia`, `Russia`, `Japan` and `SL_Indonesia`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags of the GAAP proxy.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Domain

Returns the <code>Domain</code> value.

#### ForwardIp

Returns the <code>ForwardIp</code> value.

#### Ip

Returns the <code>Ip</code> value.

#### Scalable

Returns the <code>Scalable</code> value.

#### Status

Returns the <code>Status</code> value.

#### SupportProtocols

Returns the <code>SupportProtocols</code> value.

