# Terraform::Vault::GithubAuthBackend

Manages a Github Auth mount in a Vault server. See the [Vault
documentation](https://www.vaultproject.io/docs/auth/github.html) for more
information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::GithubAuthBackend",
    "Properties" : {
        "<a href="#baseurl" title="BaseUrl">BaseUrl</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#maxttl" title="MaxTtl">MaxTtl</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#tokenboundcidrs" title="TokenBoundCidrs">TokenBoundCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#tokenexplicitmaxttl" title="TokenExplicitMaxTtl">TokenExplicitMaxTtl</a>" : <i>Double</i>,
        "<a href="#tokenmaxttl" title="TokenMaxTtl">TokenMaxTtl</a>" : <i>Double</i>,
        "<a href="#tokennodefaultpolicy" title="TokenNoDefaultPolicy">TokenNoDefaultPolicy</a>" : <i>Boolean</i>,
        "<a href="#tokennumuses" title="TokenNumUses">TokenNumUses</a>" : <i>Double</i>,
        "<a href="#tokenperiod" title="TokenPeriod">TokenPeriod</a>" : <i>Double</i>,
        "<a href="#tokenpolicies" title="TokenPolicies">TokenPolicies</a>" : <i>[ String, ... ]</i>,
        "<a href="#tokenttl" title="TokenTtl">TokenTtl</a>" : <i>Double</i>,
        "<a href="#tokentype" title="TokenType">TokenType</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>String</i>,
        "<a href="#tune" title="Tune">Tune</a>" : <i>[ <a href="tune.md">Tune</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::GithubAuthBackend
Properties:
    <a href="#baseurl" title="BaseUrl">BaseUrl</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#maxttl" title="MaxTtl">MaxTtl</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#tokenboundcidrs" title="TokenBoundCidrs">TokenBoundCidrs</a>: <i>
      - String</i>
    <a href="#tokenexplicitmaxttl" title="TokenExplicitMaxTtl">TokenExplicitMaxTtl</a>: <i>Double</i>
    <a href="#tokenmaxttl" title="TokenMaxTtl">TokenMaxTtl</a>: <i>Double</i>
    <a href="#tokennodefaultpolicy" title="TokenNoDefaultPolicy">TokenNoDefaultPolicy</a>: <i>Boolean</i>
    <a href="#tokennumuses" title="TokenNumUses">TokenNumUses</a>: <i>Double</i>
    <a href="#tokenperiod" title="TokenPeriod">TokenPeriod</a>: <i>Double</i>
    <a href="#tokenpolicies" title="TokenPolicies">TokenPolicies</a>: <i>
      - String</i>
    <a href="#tokenttl" title="TokenTtl">TokenTtl</a>: <i>Double</i>
    <a href="#tokentype" title="TokenType">TokenType</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>String</i>
    <a href="#tune" title="Tune">Tune</a>: <i>
      - <a href="tune.md">Tune</a></i>
</pre>

## Properties

#### BaseUrl

The API endpoint to use. Useful if you
are running GitHub Enterprise or an API-compatible authentication server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Specifies the description of the mount.
This overrides the current stored value, if any.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

The organization configured users must be part of.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Path where the auth backend is mounted. Defaults to `auth/github`
if not specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenBoundCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenExplicitMaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenMaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenNoDefaultPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenNumUses

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenPolicies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenType

Specifies the type of tokens that should be returned by
the mount. Valid values are "default-service", "default-batch", "service", "batch".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tune

_Required_: No

_Type_: List of <a href="tune.md">Tune</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Accessor

Returns the <code>Accessor</code> value.

#### Id

Returns the <code>Id</code> value.

