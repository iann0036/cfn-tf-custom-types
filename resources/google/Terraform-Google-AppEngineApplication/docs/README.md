# Terraform::Google::AppEngineApplication

CloudFormation equivalent of google_app_engine_application

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::AppEngineApplication",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#appid" title="AppId">AppId</a>" : <i>String</i>,
        "<a href="#authdomain" title="AuthDomain">AuthDomain</a>" : <i>String</i>,
        "<a href="#codebucket" title="CodeBucket">CodeBucket</a>" : <i>String</i>,
        "<a href="#defaultbucket" title="DefaultBucket">DefaultBucket</a>" : <i>String</i>,
        "<a href="#defaulthostname" title="DefaultHostname">DefaultHostname</a>" : <i>String</i>,
        "<a href="#gcrdomain" title="GcrDomain">GcrDomain</a>" : <i>String</i>,
        "<a href="#locationid" title="LocationId">LocationId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#servingstatus" title="ServingStatus">ServingStatus</a>" : <i>String</i>,
        "<a href="#urldispatchrule" title="UrlDispatchRule">UrlDispatchRule</a>" : <i>[ &lt;a href=&#34;urldispatchrule.md&#34;&gt;UrlDispatchRule&lt;/a&gt;, ... ]</i>,
        "<a href="#featuresettings" title="FeatureSettings">FeatureSettings</a>" : <i>[ &lt;a href=&#34;featuresettings.md&#34;&gt;FeatureSettings&lt;/a&gt;, ... ]</i>,
        "<a href="#iap" title="Iap">Iap</a>" : <i>[ &lt;a href=&#34;iap.md&#34;&gt;Iap&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::AppEngineApplication
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#appid" title="AppId">AppId</a>: <i>String</i>
    <a href="#authdomain" title="AuthDomain">AuthDomain</a>: <i>String</i>
    <a href="#codebucket" title="CodeBucket">CodeBucket</a>: <i>String</i>
    <a href="#defaultbucket" title="DefaultBucket">DefaultBucket</a>: <i>String</i>
    <a href="#defaulthostname" title="DefaultHostname">DefaultHostname</a>: <i>String</i>
    <a href="#gcrdomain" title="GcrDomain">GcrDomain</a>: <i>String</i>
    <a href="#locationid" title="LocationId">LocationId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#servingstatus" title="ServingStatus">ServingStatus</a>: <i>String</i>
    <a href="#urldispatchrule" title="UrlDispatchRule">UrlDispatchRule</a>: <i>
      - &lt;a href=&#34;urldispatchrule.md&#34;&gt;UrlDispatchRule&lt;/a&gt;</i>
    <a href="#featuresettings" title="FeatureSettings">FeatureSettings</a>: <i>
      - &lt;a href=&#34;featuresettings.md&#34;&gt;FeatureSettings&lt;/a&gt;</i>
    <a href="#iap" title="Iap">Iap</a>: <i>
      - &lt;a href=&#34;iap.md&#34;&gt;Iap&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CodeBucket

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultBucket

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultHostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcrDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

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

#### UrlDispatchRule

_Required_: No

_Type_: List of &lt;a href=&#34;urldispatchrule.md&#34;&gt;UrlDispatchRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureSettings

_Required_: No

_Type_: List of &lt;a href=&#34;featuresettings.md&#34;&gt;FeatureSettings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iap

_Required_: No

_Type_: List of &lt;a href=&#34;iap.md&#34;&gt;Iap&lt;/a&gt;

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

Returns the &lt;code&gt;AppId&lt;/code&gt; value.

#### CodeBucket

Returns the &lt;code&gt;CodeBucket&lt;/code&gt; value.

#### DefaultBucket

Returns the &lt;code&gt;DefaultBucket&lt;/code&gt; value.

#### DefaultHostname

Returns the &lt;code&gt;DefaultHostname&lt;/code&gt; value.

#### GcrDomain

Returns the &lt;code&gt;GcrDomain&lt;/code&gt; value.

#### Name

Returns the &lt;code&gt;Name&lt;/code&gt; value.

#### UrlDispatchRule

Returns the &lt;code&gt;UrlDispatchRule&lt;/code&gt; value.

