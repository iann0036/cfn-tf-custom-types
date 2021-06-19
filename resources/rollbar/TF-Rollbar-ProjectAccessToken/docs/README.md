# TF::Rollbar::ProjectAccessToken

CloudFormation equivalent of rollbar_project_access_token

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Rollbar::ProjectAccessToken",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
        "<a href="#ratelimitwindowcount" title="RateLimitWindowCount">RateLimitWindowCount</a>" : <i>Double</i>,
        "<a href="#ratelimitwindowsize" title="RateLimitWindowSize">RateLimitWindowSize</a>" : <i>Double</i>,
        "<a href="#scopes" title="Scopes">Scopes</a>" : <i>[ String, ... ]</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Rollbar::ProjectAccessToken
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
    <a href="#ratelimitwindowcount" title="RateLimitWindowCount">RateLimitWindowCount</a>: <i>Double</i>
    <a href="#ratelimitwindowsize" title="RateLimitWindowSize">RateLimitWindowSize</a>: <i>Double</i>
    <a href="#scopes" title="Scopes">Scopes</a>: <i>
      - String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimitWindowCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimitWindowSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scopes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

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

#### AccessToken

Returns the <code>AccessToken</code> value.

#### CurRateLimitWindowCount

Returns the <code>CurRateLimitWindowCount</code> value.

#### CurRateLimitWindowStart

Returns the <code>CurRateLimitWindowStart</code> value.

#### DateCreated

Returns the <code>DateCreated</code> value.

#### DateModified

Returns the <code>DateModified</code> value.

#### Id

Returns the <code>Id</code> value.

