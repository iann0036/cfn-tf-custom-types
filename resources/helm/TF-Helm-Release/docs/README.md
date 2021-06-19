# TF::Helm::Release

A Release is an instance of a chart running in a Kubernetes cluster.

A Chart is a Helm package. It contains all of the resource definitions necessary to run an application, tool, or service inside of a Kubernetes cluster.

`helm_release` describes the desired status of a chart in a kubernetes cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Helm::Release",
    "Properties" : {
        "<a href="#atomic" title="Atomic">Atomic</a>" : <i>Boolean</i>,
        "<a href="#chart" title="Chart">Chart</a>" : <i>String</i>,
        "<a href="#cleanuponfail" title="CleanupOnFail">CleanupOnFail</a>" : <i>Boolean</i>,
        "<a href="#createnamespace" title="CreateNamespace">CreateNamespace</a>" : <i>Boolean</i>,
        "<a href="#dependencyupdate" title="DependencyUpdate">DependencyUpdate</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#devel" title="Devel">Devel</a>" : <i>Boolean</i>,
        "<a href="#disablecrdhooks" title="DisableCrdHooks">DisableCrdHooks</a>" : <i>Boolean</i>,
        "<a href="#disableopenapivalidation" title="DisableOpenapiValidation">DisableOpenapiValidation</a>" : <i>Boolean</i>,
        "<a href="#disablewebhooks" title="DisableWebhooks">DisableWebhooks</a>" : <i>Boolean</i>,
        "<a href="#forceupdate" title="ForceUpdate">ForceUpdate</a>" : <i>Boolean</i>,
        "<a href="#keyring" title="Keyring">Keyring</a>" : <i>String</i>,
        "<a href="#lint" title="Lint">Lint</a>" : <i>Boolean</i>,
        "<a href="#maxhistory" title="MaxHistory">MaxHistory</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#recreatepods" title="RecreatePods">RecreatePods</a>" : <i>Boolean</i>,
        "<a href="#rendersubchartnotes" title="RenderSubchartNotes">RenderSubchartNotes</a>" : <i>Boolean</i>,
        "<a href="#replace" title="Replace">Replace</a>" : <i>Boolean</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>,
        "<a href="#repositorycafile" title="RepositoryCaFile">RepositoryCaFile</a>" : <i>String</i>,
        "<a href="#repositorycertfile" title="RepositoryCertFile">RepositoryCertFile</a>" : <i>String</i>,
        "<a href="#repositorykeyfile" title="RepositoryKeyFile">RepositoryKeyFile</a>" : <i>String</i>,
        "<a href="#repositorypassword" title="RepositoryPassword">RepositoryPassword</a>" : <i>String</i>,
        "<a href="#repositoryusername" title="RepositoryUsername">RepositoryUsername</a>" : <i>String</i>,
        "<a href="#resetvalues" title="ResetValues">ResetValues</a>" : <i>Boolean</i>,
        "<a href="#reusevalues" title="ReuseValues">ReuseValues</a>" : <i>Boolean</i>,
        "<a href="#skipcrds" title="SkipCrds">SkipCrds</a>" : <i>Boolean</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#values" title="Values">Values</a>" : <i>[ String, ... ]</i>,
        "<a href="#verify" title="Verify">Verify</a>" : <i>Boolean</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#wait" title="Wait">Wait</a>" : <i>Boolean</i>,
        "<a href="#waitforjobs" title="WaitForJobs">WaitForJobs</a>" : <i>Boolean</i>,
        "<a href="#postrender" title="Postrender">Postrender</a>" : <i>[ <a href="postrenderdefinition.md">PostrenderDefinition</a>, ... ]</i>,
        "<a href="#set" title="Set">Set</a>" : <i>[ <a href="setdefinition.md">SetDefinition</a>, ... ]</i>,
        "<a href="#setsensitive" title="SetSensitive">SetSensitive</a>" : <i>[ <a href="setsensitivedefinition.md">SetSensitiveDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Helm::Release
Properties:
    <a href="#atomic" title="Atomic">Atomic</a>: <i>Boolean</i>
    <a href="#chart" title="Chart">Chart</a>: <i>String</i>
    <a href="#cleanuponfail" title="CleanupOnFail">CleanupOnFail</a>: <i>Boolean</i>
    <a href="#createnamespace" title="CreateNamespace">CreateNamespace</a>: <i>Boolean</i>
    <a href="#dependencyupdate" title="DependencyUpdate">DependencyUpdate</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#devel" title="Devel">Devel</a>: <i>Boolean</i>
    <a href="#disablecrdhooks" title="DisableCrdHooks">DisableCrdHooks</a>: <i>Boolean</i>
    <a href="#disableopenapivalidation" title="DisableOpenapiValidation">DisableOpenapiValidation</a>: <i>Boolean</i>
    <a href="#disablewebhooks" title="DisableWebhooks">DisableWebhooks</a>: <i>Boolean</i>
    <a href="#forceupdate" title="ForceUpdate">ForceUpdate</a>: <i>Boolean</i>
    <a href="#keyring" title="Keyring">Keyring</a>: <i>String</i>
    <a href="#lint" title="Lint">Lint</a>: <i>Boolean</i>
    <a href="#maxhistory" title="MaxHistory">MaxHistory</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#recreatepods" title="RecreatePods">RecreatePods</a>: <i>Boolean</i>
    <a href="#rendersubchartnotes" title="RenderSubchartNotes">RenderSubchartNotes</a>: <i>Boolean</i>
    <a href="#replace" title="Replace">Replace</a>: <i>Boolean</i>
    <a href="#repository" title="Repository">Repository</a>: <i>String</i>
    <a href="#repositorycafile" title="RepositoryCaFile">RepositoryCaFile</a>: <i>String</i>
    <a href="#repositorycertfile" title="RepositoryCertFile">RepositoryCertFile</a>: <i>String</i>
    <a href="#repositorykeyfile" title="RepositoryKeyFile">RepositoryKeyFile</a>: <i>String</i>
    <a href="#repositorypassword" title="RepositoryPassword">RepositoryPassword</a>: <i>String</i>
    <a href="#repositoryusername" title="RepositoryUsername">RepositoryUsername</a>: <i>String</i>
    <a href="#resetvalues" title="ResetValues">ResetValues</a>: <i>Boolean</i>
    <a href="#reusevalues" title="ReuseValues">ReuseValues</a>: <i>Boolean</i>
    <a href="#skipcrds" title="SkipCrds">SkipCrds</a>: <i>Boolean</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#values" title="Values">Values</a>: <i>
      - String</i>
    <a href="#verify" title="Verify">Verify</a>: <i>Boolean</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#wait" title="Wait">Wait</a>: <i>Boolean</i>
    <a href="#waitforjobs" title="WaitForJobs">WaitForJobs</a>: <i>Boolean</i>
    <a href="#postrender" title="Postrender">Postrender</a>: <i>
      - <a href="postrenderdefinition.md">PostrenderDefinition</a></i>
    <a href="#set" title="Set">Set</a>: <i>
      - <a href="setdefinition.md">SetDefinition</a></i>
    <a href="#setsensitive" title="SetSensitive">SetSensitive</a>: <i>
      - <a href="setsensitivedefinition.md">SetSensitiveDefinition</a></i>
</pre>

## Properties

#### Atomic

If set, installation process purges chart on fail. The wait flag will be set automatically if atomic is used. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Chart

Chart name to be installed. The chart name can be local path, a URL to a chart, or the name of the chart if `repository` is specified. It is also possible to use the `<repository>/<chart>` format here if you are running Terraform on a system that the repository has been added to with `helm repo add` but this is not recommended.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CleanupOnFail

Allow deletion of new resources created in this upgrade when upgrade fails. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateNamespace

Create the namespace if it does not yet exist. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DependencyUpdate

Runs helm dependency update before installing the chart. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Set release description attribute (visible in the history).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Devel

Use chart development versions, too. Equivalent to version '>0.0.0-0'. If version is set, this is ignored.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableCrdHooks

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableOpenapiValidation

If set, the installation process will not validate rendered templates against the Kubernetes OpenAPI Schema. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableWebhooks

Prevent hooks from running. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceUpdate

Force resource update through delete/recreate if needed. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keyring

Location of public keys used for verification. Used only if `verify` is true. Defaults to `/.gnupg/pubring.gpg` in the location set by `home`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lint

Run the helm chart linter during the plan. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHistory

Maximum number of release versions stored per release. Defaults to `0` (no limit).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Release name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

The namespace to install the release into. Defaults to `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecreatePods

Perform pods restart during upgrade/rollback. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenderSubchartNotes

If set, render subchart notes along with the parent. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replace

Re-use the given name, even if that name is already used. This is unsafe in production. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

Repository URL where to locate the requested chart.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepositoryCaFile

The Repositories CA File.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepositoryCertFile

The repositories cert file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepositoryKeyFile

The repositories cert key file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepositoryPassword

Password for HTTP basic authentication against the repository.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepositoryUsername

Username for HTTP basic authentication against the repository.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetValues

When upgrading, reset the values to the ones built into the chart. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReuseValues

When upgrading, reuse the last release's values and merge in any overrides. If 'reset_values' is specified, this is ignored. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipCrds

If set, no CRDs will be installed. By default, CRDs are installed if not already present. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Time in seconds to wait for any individual kubernetes operation (like Jobs for hooks). Defaults to `300` seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Values

List of values in raw yaml to pass to helm. Values will be merged, in order, as Helm does with multiple `-f` options.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Verify

Verify the package before installing it. Helm uses a provenance file to verify the integrity of the chart; this must be hosted alongside the chart. For more information see the [Helm Documentation](https://helm.sh/docs/topics/provenance/). Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Specify the exact chart version to install. If this is not specified, the latest version is installed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wait

Will wait until all resources are in a ready state before marking the release as successful. It will wait for as long as `timeout`. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForJobs

If wait is enabled, will wait until all Jobs have been completed before marking the release as successful. It will wait for as long as `timeout`.  Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Postrender

_Required_: No

_Type_: List of <a href="postrenderdefinition.md">PostrenderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Set

_Required_: No

_Type_: List of <a href="setdefinition.md">SetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetSensitive

_Required_: No

_Type_: List of <a href="setsensitivedefinition.md">SetSensitiveDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Manifest

Returns the <code>Manifest</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### Status

Returns the <code>Status</code> value.

