# Terraform::Tfe::OauthClient

An OAuth Client represents the connection between an organization and a VCS
provider.

-> **Note:** This resource does not currently support creation of Bitbucket
  Server OAuth clients.

-> **Note:** This resource requires a private key when creating Azure DevOps Server OAuth clients.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Tfe::OauthClient",
    "Properties" : {
        "<a href="#apiurl" title="ApiUrl">ApiUrl</a>" : <i>String</i>,
        "<a href="#httpurl" title="HttpUrl">HttpUrl</a>" : <i>String</i>,
        "<a href="#oauthtoken" title="OauthToken">OauthToken</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>String</i>,
        "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>,
        "<a href="#serviceprovider" title="ServiceProvider">ServiceProvider</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Tfe::OauthClient
Properties:
    <a href="#apiurl" title="ApiUrl">ApiUrl</a>: <i>String</i>
    <a href="#httpurl" title="HttpUrl">HttpUrl</a>: <i>String</i>
    <a href="#oauthtoken" title="OauthToken">OauthToken</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>String</i>
    <a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
    <a href="#serviceprovider" title="ServiceProvider">ServiceProvider</a>: <i>String</i>
</pre>

## Properties

#### ApiUrl

The base URL of your VCS provider's API (e.g.
`https://api.github.com` or `https://ghe.example.com/api/v3`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpUrl

The homepage of your VCS provider (e.g.
`https://github.com` or `https://ghe.example.com`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OauthToken

The token string you were given by your VCS provider.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

Name of the organization.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

The text of the private key associated with your Azure DevOps Server account.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceProvider

The VCS provider being connected with. Valid
options are `ado_server`, `ado_services`, `github`, `github_enterprise`, `gitlab_hosted`,
`gitlab_community_edition`, or `gitlab_enterprise_edition`.

_Required_: Yes

_Type_: String

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

#### OauthTokenId

Returns the <code>OauthTokenId</code> value.

