# Terraform::Google::AppEngineApplication

CloudFormation equivalent of google_app_engine_application

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::AppEngineApplication",
    "Properties" : {
        "<a href="#authdomain" title="AuthDomain">AuthDomain</a>" : <i>String</i>,
        "<a href="#locationid" title="LocationId">LocationId</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#servingstatus" title="ServingStatus">ServingStatus</a>" : <i>String</i>,
        "<a href="#featuresettings" title="FeatureSettings">FeatureSettings</a>" : <i>[ <a href="featuresettings.md">FeatureSettings</a>, ... ]</i>,
        "<a href="#iap" title="Iap">Iap</a>" : <i>[ <a href="iap.md">Iap</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::AppEngineApplication
Properties:
    <a href="#authdomain" title="AuthDomain">AuthDomain</a>: <i>String</i>
    <a href="#locationid" title="LocationId">LocationId</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#servingstatus" title="ServingStatus">ServingStatus</a>: <i>String</i>
    <a href="#featuresettings" title="FeatureSettings">FeatureSettings</a>: <i>
      - <a href="featuresettings.md">FeatureSettings</a></i>
    <a href="#iap" title="Iap">Iap</a>: <i>
      - <a href="iap.md">Iap</a></i>
</pre>

## Properties

#### AuthDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServingStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureSettings

_Required_: No

_Type_: List of <a href="featuresettings.md">FeatureSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iap

_Required_: No

_Type_: List of <a href="iap.md">Iap</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AppId

Returns the <code>AppId</code> value.

#### CodeBucket

Returns the <code>CodeBucket</code> value.

#### DefaultBucket

Returns the <code>DefaultBucket</code> value.

#### DefaultHostname

Returns the <code>DefaultHostname</code> value.

#### GcrDomain

Returns the <code>GcrDomain</code> value.

#### Name

Returns the <code>Name</code> value.

#### UrlDispatchRule

Returns the <code>UrlDispatchRule</code> value.

