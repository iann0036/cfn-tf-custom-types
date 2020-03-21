# Terraform::Google::AppEngineStandardAppVersion

Standard App Version resource to create a new version of standard GAE Application.
Currently supporting Zip and File Containers.
Currently does not support async operation checking.


To get more information about StandardAppVersion, see:

* [API documentation](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/appengine/docs/standard)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=app_engine_standard_app_version&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::AppEngineStandardAppVersion",
    "Properties" : {
        "<a href="#deleteserviceondestroy" title="DeleteServiceOnDestroy">DeleteServiceOnDestroy</a>" : <i>Boolean</i>,
        "<a href="#envvariables" title="EnvVariables">EnvVariables</a>" : <i>[ <a href="envvariables.md">EnvVariables</a>, ... ]</i>,
        "<a href="#instanceclass" title="InstanceClass">InstanceClass</a>" : <i>String</i>,
        "<a href="#noopondestroy" title="NoopOnDestroy">NoopOnDestroy</a>" : <i>Boolean</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
        "<a href="#runtimeapiversion" title="RuntimeApiVersion">RuntimeApiVersion</a>" : <i>String</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#threadsafe" title="Threadsafe">Threadsafe</a>" : <i>Boolean</i>,
        "<a href="#versionid" title="VersionId">VersionId</a>" : <i>String</i>,
        "<a href="#deployment" title="Deployment">Deployment</a>" : <i>[ <a href="deployment.md">Deployment</a>, ... ]</i>,
        "<a href="#entrypoint" title="Entrypoint">Entrypoint</a>" : <i>[ <a href="entrypoint.md">Entrypoint</a>, ... ]</i>,
        "<a href="#handlers" title="Handlers">Handlers</a>" : <i>[ <a href="handlers.md">Handlers</a>, ... ]</i>,
        "<a href="#libraries" title="Libraries">Libraries</a>" : <i>[ <a href="libraries.md">Libraries</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#files" title="Files">Files</a>" : <i>[ <a href="files.md">Files</a>, ... ]</i>,
        "<a href="#zip" title="Zip">Zip</a>" : <i>[ <a href="zip.md">Zip</a>, ... ]</i>,
        "<a href="#script" title="Script">Script</a>" : <i>[ <a href="script.md">Script</a>, ... ]</i>,
        "<a href="#staticfiles" title="StaticFiles">StaticFiles</a>" : <i>[ <a href="staticfiles.md">StaticFiles</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::AppEngineStandardAppVersion
Properties:
    <a href="#deleteserviceondestroy" title="DeleteServiceOnDestroy">DeleteServiceOnDestroy</a>: <i>Boolean</i>
    <a href="#envvariables" title="EnvVariables">EnvVariables</a>: <i>
      - <a href="envvariables.md">EnvVariables</a></i>
    <a href="#instanceclass" title="InstanceClass">InstanceClass</a>: <i>String</i>
    <a href="#noopondestroy" title="NoopOnDestroy">NoopOnDestroy</a>: <i>Boolean</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
    <a href="#runtimeapiversion" title="RuntimeApiVersion">RuntimeApiVersion</a>: <i>String</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#threadsafe" title="Threadsafe">Threadsafe</a>: <i>Boolean</i>
    <a href="#versionid" title="VersionId">VersionId</a>: <i>String</i>
    <a href="#deployment" title="Deployment">Deployment</a>: <i>
      - <a href="deployment.md">Deployment</a></i>
    <a href="#entrypoint" title="Entrypoint">Entrypoint</a>: <i>
      - <a href="entrypoint.md">Entrypoint</a></i>
    <a href="#handlers" title="Handlers">Handlers</a>: <i>
      - <a href="handlers.md">Handlers</a></i>
    <a href="#libraries" title="Libraries">Libraries</a>: <i>
      - <a href="libraries.md">Libraries</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#files" title="Files">Files</a>: <i>
      - <a href="files.md">Files</a></i>
    <a href="#zip" title="Zip">Zip</a>: <i>
      - <a href="zip.md">Zip</a></i>
    <a href="#script" title="Script">Script</a>: <i>
      - <a href="script.md">Script</a></i>
    <a href="#staticfiles" title="StaticFiles">StaticFiles</a>: <i>
      - <a href="staticfiles.md">StaticFiles</a></i>
</pre>

## Properties

#### DeleteServiceOnDestroy

If set to `true`, the service will be deleted if it is the last version.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvVariables

_Required_: No

_Type_: List of <a href="envvariables.md">EnvVariables</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceClass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoopOnDestroy

If set to `true`, the application version will not be deleted.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuntimeApiVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threadsafe

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deployment

_Required_: No

_Type_: List of <a href="deployment.md">Deployment</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entrypoint

_Required_: No

_Type_: List of <a href="entrypoint.md">Entrypoint</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Handlers

_Required_: No

_Type_: List of <a href="handlers.md">Handlers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Libraries

_Required_: No

_Type_: List of <a href="libraries.md">Libraries</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Files

_Required_: No

_Type_: List of <a href="files.md">Files</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zip

_Required_: No

_Type_: List of <a href="zip.md">Zip</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Script

_Required_: No

_Type_: List of <a href="script.md">Script</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticFiles

_Required_: No

_Type_: List of <a href="staticfiles.md">StaticFiles</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Name

Returns the <code>Name</code> value.

