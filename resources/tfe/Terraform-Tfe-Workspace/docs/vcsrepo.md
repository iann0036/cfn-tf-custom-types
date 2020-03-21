# Terraform::Tfe::Workspace VcsRepo

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#branch" title="Branch">Branch</a>" : <i>String</i>,
    "<a href="#identifier" title="Identifier">Identifier</a>" : <i>String</i>,
    "<a href="#ingresssubmodules" title="IngressSubmodules">IngressSubmodules</a>" : <i>Boolean</i>,
    "<a href="#oauthtokenid" title="OauthTokenId">OauthTokenId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#branch" title="Branch">Branch</a>: <i>String</i>
<a href="#identifier" title="Identifier">Identifier</a>: <i>String</i>
<a href="#ingresssubmodules" title="IngressSubmodules">IngressSubmodules</a>: <i>Boolean</i>
<a href="#oauthtokenid" title="OauthTokenId">OauthTokenId</a>: <i>String</i>
</pre>

## Properties

#### Branch

The repository branch that Terraform will execute from.
Default to `master`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identifier

A reference to your VCS repository in the format
`:org/:repo` where `:org` and `:repo` refer to the organization and repository
in your VCS provider.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressSubmodules

Whether submodules should be fetched when
cloning the VCS repository. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OauthTokenId

Token ID of the VCS Connection (OAuth Conection Token)
to use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

