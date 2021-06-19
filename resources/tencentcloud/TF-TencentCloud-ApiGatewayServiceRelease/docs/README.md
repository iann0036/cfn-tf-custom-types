# TF::TencentCloud::ApiGatewayServiceRelease

Use this resource to create API gateway service release.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ApiGatewayServiceRelease",
    "Properties" : {
        "<a href="#environmentname" title="EnvironmentName">EnvironmentName</a>" : <i>String</i>,
        "<a href="#releasedesc" title="ReleaseDesc">ReleaseDesc</a>" : <i>String</i>,
        "<a href="#releaseversion" title="ReleaseVersion">ReleaseVersion</a>" : <i>String</i>,
        "<a href="#serviceid" title="ServiceId">ServiceId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ApiGatewayServiceRelease
Properties:
    <a href="#environmentname" title="EnvironmentName">EnvironmentName</a>: <i>String</i>
    <a href="#releasedesc" title="ReleaseDesc">ReleaseDesc</a>: <i>String</i>
    <a href="#releaseversion" title="ReleaseVersion">ReleaseVersion</a>: <i>String</i>
    <a href="#serviceid" title="ServiceId">ServiceId</a>: <i>String</i>
</pre>

## Properties

#### EnvironmentName

API gateway service environment name to be released. Valid values: `test`, `prepub`, `release`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReleaseDesc

This release description of the API gateway service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReleaseVersion

The release version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceId

ID of API gateway service.

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

