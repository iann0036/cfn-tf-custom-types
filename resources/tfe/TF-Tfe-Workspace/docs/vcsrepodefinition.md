# TF::Tfe::Workspace VcsRepoDefinition

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
This defaults to the repository's default branch (e.g. main).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identifier

A reference to your VCS repository in the format
`<organization>/<repository>` where `<organization>` and `<repository>` refer to the organization and repository
in your VCS provider. The format for Azure DevOps is <organization>/<project>/_git/<repository>.

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

The VCS Connection (OAuth Connection + Token) to use.
This ID can be obtained from a `tfe_oauth_client` resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

