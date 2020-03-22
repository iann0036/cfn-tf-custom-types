# Terraform::Heroku::Slug

Provides a [Heroku Slug](https://devcenter.heroku.com/articles/platform-api-reference#slug)
resource.

This resource supports uploading a pre-generated archive file of executable code, making it possible to launch apps directly from a Terraform config. This resource does not itself generate the slug archive. [A guide to creating slug archives](https://devcenter.heroku.com/articles/platform-api-deploying-slugs) is available in the Heroku Dev Center.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::Slug",
    "Properties" : {
        "<a href="#app" title="App">App</a>" : <i>String</i>,
        "<a href="#buildpackprovideddescription" title="BuildpackProvidedDescription">BuildpackProvidedDescription</a>" : <i>String</i>,
        "<a href="#checksum" title="Checksum">Checksum</a>" : <i>String</i>,
        "<a href="#commit" title="Commit">Commit</a>" : <i>String</i>,
        "<a href="#commitdescription" title="CommitDescription">CommitDescription</a>" : <i>String</i>,
        "<a href="#filepath" title="FilePath">FilePath</a>" : <i>String</i>,
        "<a href="#fileurl" title="FileUrl">FileUrl</a>" : <i>String</i>,
        "<a href="#processtypes" title="ProcessTypes">ProcessTypes</a>" : <i>[ <a href="processtypes.md">ProcessTypes</a>, ... ]</i>,
        "<a href="#stack" title="Stack">Stack</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::Slug
Properties:
    <a href="#app" title="App">App</a>: <i>String</i>
    <a href="#buildpackprovideddescription" title="BuildpackProvidedDescription">BuildpackProvidedDescription</a>: <i>String</i>
    <a href="#checksum" title="Checksum">Checksum</a>: <i>String</i>
    <a href="#commit" title="Commit">Commit</a>: <i>String</i>
    <a href="#commitdescription" title="CommitDescription">CommitDescription</a>: <i>String</i>
    <a href="#filepath" title="FilePath">FilePath</a>: <i>String</i>
    <a href="#fileurl" title="FileUrl">FileUrl</a>: <i>String</i>
    <a href="#processtypes" title="ProcessTypes">ProcessTypes</a>: <i>
      - <a href="processtypes.md">ProcessTypes</a></i>
    <a href="#stack" title="Stack">Stack</a>: <i>String</i>
</pre>

## Properties

#### App

The ID of the Heroku app.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildpackProvidedDescription

Description of language or app framework, `"Ruby/Rack"`; displayed as the app's language in the Heroku Dashboard.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Checksum

Hash of the slug for verifying its integrity, auto-generated from contents of `file_path` or `file_url`, `SHA256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Commit

Identification of the code with your version control system (eg: SHA of the git HEAD), `"60883d9e8947a57e04dc9124f25df004866a2051"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommitDescription

Description of the provided commit.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilePath

Local path to a slug archive, `"slugs/current.tgz"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileUrl

**https** URL to a slug archive, `"https://example.com/slugs/app-v1.tgz"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessTypes

Map of [processes to launch on Heroku Dynos](https://devcenter.heroku.com/articles/process-model).

_Required_: Yes

_Type_: List of <a href="processtypes.md">ProcessTypes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stack

Name or ID of the [Heroku stack](https://devcenter.heroku.com/articles/stack).

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

#### Blob

Returns the <code>Blob</code> value.

#### Id

Returns the <code>Id</code> value.

#### Size

Returns the <code>Size</code> value.

#### StackId

Returns the <code>StackId</code> value.

