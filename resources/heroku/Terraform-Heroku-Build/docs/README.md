# Terraform::Heroku::Build

Provides a [Heroku Build](https://devcenter.heroku.com/articles/platform-api-reference#build)
resource, to deploy source code to a Heroku app.

Either a [URL](#source-urls) or [local path](#local-source), pointing to a [tarball](https://en.wikipedia.org/wiki/Tar_(computing)) of the source code, may be deployed. If a local path is used, it may instead point to a directory of source code, which will be tarballed automatically and then deployed.

This resource waits until the [build](https://devcenter.heroku.com/articles/build-and-release-using-the-api) & [release](https://devcenter.heroku.com/articles/release-phase) completes.

If the build fails, the error will contain a URL to view the build log. `curl "https://the-long-log-url-in-the-error"`.

To start the app from a successful build, use a [Formation resource](formation.html) to specify the process, dyno size, and dyno quantity.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::Build",
    "Properties" : {
        "<a href="#app" title="App">App</a>" : <i>String</i>,
        "<a href="#buildpacks" title="Buildpacks">Buildpacks</a>" : <i>[ String, ... ]</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ <a href="source.md">Source</a>, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::Build
Properties:
    <a href="#app" title="App">App</a>: <i>String</i>
    <a href="#buildpacks" title="Buildpacks">Buildpacks</a>: <i>
      - String</i>
    <a href="#source" title="Source">Source</a>: <i>
      - <a href="source.md">Source</a></i>
</pre>

## Properties

#### App

The ID of the Heroku app.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Buildpacks

List of buildpack GitHub URLs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

A block that specifies the source code to build & release:
* `checksum` - Hash of the source archive for verifying its integrity, auto-generated when `source.path` is set, `SHA256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
* `path` - (Required unless `source.url` is set) Local path to the source directory or tarball archive for the app
* `url` - (Required unless `source.path` is set) `https` location of the source archive for the app
* `version` - Use to track what version of your source originated this build. If you are creating builds from git-versioned source code, for example, the commit hash, or release tag would be a good value to use for the version parameter.

_Required_: Yes

_Type_: List of <a href="source.md">Source</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### LocalChecksum

Returns the <code>LocalChecksum</code> value.

#### OutputStreamUrl

Returns the <code>OutputStreamUrl</code> value.

#### ReleaseId

Returns the <code>ReleaseId</code> value.

#### SlugId

Returns the <code>SlugId</code> value.

#### Stack

Returns the <code>Stack</code> value.

#### Status

Returns the <code>Status</code> value.

#### User

Returns the <code>User</code> value.

#### Uuid

Returns the <code>Uuid</code> value.

