# TF::Tfe::RegistryModule VcsRepoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#displayidentifier" title="DisplayIdentifier">DisplayIdentifier</a>" : <i>String</i>,
    "<a href="#identifier" title="Identifier">Identifier</a>" : <i>String</i>,
    "<a href="#oauthtokenid" title="OauthTokenId">OauthTokenId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#displayidentifier" title="DisplayIdentifier">DisplayIdentifier</a>: <i>String</i>
<a href="#identifier" title="Identifier">Identifier</a>: <i>String</i>
<a href="#oauthtokenid" title="OauthTokenId">OauthTokenId</a>: <i>String</i>
</pre>

## Properties

#### DisplayIdentifier

The display identifier for your VCS repository.
For most VCS providers outside of BitBucket Cloud, this will match the `identifier`
string.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identifier

A reference to your VCS repository in the format
`<organization>/<repository>` where `<organization>` and `<repository>` refer to the organization (or project key, for Bitbucket Server)
and repository in your VCS provider. The format for Azure DevOps is <organization>/<project>/_git/<repository>.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OauthTokenId

Token ID of the VCS Connection (OAuth Connection Token)
to use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

