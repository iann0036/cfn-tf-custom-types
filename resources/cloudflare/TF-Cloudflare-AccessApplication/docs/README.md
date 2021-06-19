# TF::Cloudflare::AccessApplication

Provides a Cloudflare Access Application resource. Access Applications
are used to restrict access to a whole application using an
authorisation gateway managed by Cloudflare.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudflare::AccessApplication",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#allowedidps" title="AllowedIdps">AllowedIdps</a>" : <i>[ String, ... ]</i>,
        "<a href="#autoredirecttoidentity" title="AutoRedirectToIdentity">AutoRedirectToIdentity</a>" : <i>Boolean</i>,
        "<a href="#customdenymessage" title="CustomDenyMessage">CustomDenyMessage</a>" : <i>String</i>,
        "<a href="#customdenyurl" title="CustomDenyUrl">CustomDenyUrl</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#enablebindingcookie" title="EnableBindingCookie">EnableBindingCookie</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sessionduration" title="SessionDuration">SessionDuration</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#corsheaders" title="CorsHeaders">CorsHeaders</a>" : <i>[ <a href="corsheadersdefinition.md">CorsHeadersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudflare::AccessApplication
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#allowedidps" title="AllowedIdps">AllowedIdps</a>: <i>
      - String</i>
    <a href="#autoredirecttoidentity" title="AutoRedirectToIdentity">AutoRedirectToIdentity</a>: <i>Boolean</i>
    <a href="#customdenymessage" title="CustomDenyMessage">CustomDenyMessage</a>: <i>String</i>
    <a href="#customdenyurl" title="CustomDenyUrl">CustomDenyUrl</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#enablebindingcookie" title="EnableBindingCookie">EnableBindingCookie</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sessionduration" title="SessionDuration">SessionDuration</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#corsheaders" title="CorsHeaders">CorsHeaders</a>: <i>
      - <a href="corsheadersdefinition.md">CorsHeadersDefinition</a></i>
</pre>

## Properties

#### AccountId

The account to which the access application should be added. Conflicts with `zone_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedIdps

The identity providers selected for the application.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRedirectToIdentity

Option to skip identity provider
selection if only one is configured in allowed_idps. Defaults to `false`
(disabled).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomDenyMessage

Option that returns a custom error message when a user is denied access to the application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomDenyUrl

Option that redirects to a custom URL when a user is denied access to the application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

The complete URL of the asset you wish to put
Cloudflare Access in front of. Can include subdomains or paths. Or both.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBindingCookie

Option to provide increased security against compromised authorization tokens and CSRF attacks by requiring an additional "binding" cookie on requests. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Friendly name of the Access Application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionDuration

How often a user will be forced to
re-authorise. Must be in the format `"48h"` or `"2h45m"`.
Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`. Defaults to `24h`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The DNS zone to which the access application should be added. Conflicts with `account_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsHeaders

_Required_: No

_Type_: List of <a href="corsheadersdefinition.md">CorsHeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Aud

Returns the <code>Aud</code> value.

#### Id

Returns the <code>Id</code> value.

