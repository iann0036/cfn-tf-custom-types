# Terraform::NSXT::LbCookiePersistenceProfile

Provides a resource to configure lb cookie persistence profile on NSX-T manager

~> **NOTE:** This resource requires NSX version 2.3 or higher.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::LbCookiePersistenceProfile",
    "Properties" : {
        "<a href="#cookiefallback" title="CookieFallback">CookieFallback</a>" : <i>Boolean</i>,
        "<a href="#cookiegarble" title="CookieGarble">CookieGarble</a>" : <i>Boolean</i>,
        "<a href="#cookiemode" title="CookieMode">CookieMode</a>" : <i>String</i>,
        "<a href="#cookiename" title="CookieName">CookieName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#persistenceshared" title="PersistenceShared">PersistenceShared</a>" : <i>Boolean</i>,
        "<a href="#insertmodeparams" title="InsertModeParams">InsertModeParams</a>" : <i>[ <a href="insertmodeparams.md">InsertModeParams</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::LbCookiePersistenceProfile
Properties:
    <a href="#cookiefallback" title="CookieFallback">CookieFallback</a>: <i>Boolean</i>
    <a href="#cookiegarble" title="CookieGarble">CookieGarble</a>: <i>Boolean</i>
    <a href="#cookiemode" title="CookieMode">CookieMode</a>: <i>String</i>
    <a href="#cookiename" title="CookieName">CookieName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#persistenceshared" title="PersistenceShared">PersistenceShared</a>: <i>Boolean</i>
    <a href="#insertmodeparams" title="InsertModeParams">InsertModeParams</a>: <i>
      - <a href="insertmodeparams.md">InsertModeParams</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tag.md">Tag</a></i>
</pre>

## Properties

#### CookieFallback

A boolean flag which reflects whether once the server points by this cookie is down, a new server is selected, or the requests will be rejected.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieGarble

A boolean flag which reflects whether the cookie value (server IP and port) would be encrypted or in plain text.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieMode

The cookie persistence mode. Accepted values: PREFIX, REWRITE and INSERT which is the default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieName

cookie name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name of this resource. Defaults to ID if not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistenceShared

A boolean flag which reflects whether the cookie persistence is private or shared. When false (which is the default value), the cookie persistence is private to each virtual server and is qualified by the pool. If set to true, in cookie insert mode, cookie persistence could be shared across multiple virtual servers that are bound to the same pools.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertModeParams

_Required_: No

_Type_: List of <a href="insertmodeparams.md">InsertModeParams</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tag.md">Tag</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Revision

Returns the <code>Revision</code> value.

