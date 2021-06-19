# TF::Google::CloudfunctionsFunction

Creates a new Cloud Function. For more information see:

* [API documentation](https://cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/functions/docs)


~> **Warning:** As of November 1, 2019, newly created Functions are
private-by-default and will require [appropriate IAM permissions](https://cloud.google.com/functions/docs/reference/iam/roles)
to be invoked. See below examples for how to set up the appropriate permissions,
or view the [Cloud Functions IAM resources](/docs/providers/google/r/cloudfunctions_cloud_function_iam.html)
for Cloud Functions.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::CloudfunctionsFunction",
    "Properties" : {
        "<a href="#availablememorymb" title="AvailableMemoryMb">AvailableMemoryMb</a>" : <i>Double</i>,
        "<a href="#buildenvironmentvariables" title="BuildEnvironmentVariables">BuildEnvironmentVariables</a>" : <i>[ <a href="buildenvironmentvariablesdefinition.md">BuildEnvironmentVariablesDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#entrypoint" title="EntryPoint">EntryPoint</a>" : <i>String</i>,
        "<a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>" : <i>[ <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>, ... ]</i>,
        "<a href="#httpstriggerurl" title="HttpsTriggerUrl">HttpsTriggerUrl</a>" : <i>String</i>,
        "<a href="#ingresssettings" title="IngressSettings">IngressSettings</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#maxinstances" title="MaxInstances">MaxInstances</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
        "<a href="#serviceaccountemail" title="ServiceAccountEmail">ServiceAccountEmail</a>" : <i>String</i>,
        "<a href="#sourcearchivebucket" title="SourceArchiveBucket">SourceArchiveBucket</a>" : <i>String</i>,
        "<a href="#sourcearchiveobject" title="SourceArchiveObject">SourceArchiveObject</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#triggerhttp" title="TriggerHttp">TriggerHttp</a>" : <i>Boolean</i>,
        "<a href="#vpcconnector" title="VpcConnector">VpcConnector</a>" : <i>String</i>,
        "<a href="#vpcconnectoregresssettings" title="VpcConnectorEgressSettings">VpcConnectorEgressSettings</a>" : <i>String</i>,
        "<a href="#eventtrigger" title="EventTrigger">EventTrigger</a>" : <i>[ <a href="eventtriggerdefinition.md">EventTriggerDefinition</a>, ... ]</i>,
        "<a href="#sourcerepository" title="SourceRepository">SourceRepository</a>" : <i>[ <a href="sourcerepositorydefinition.md">SourceRepositoryDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::CloudfunctionsFunction
Properties:
    <a href="#availablememorymb" title="AvailableMemoryMb">AvailableMemoryMb</a>: <i>Double</i>
    <a href="#buildenvironmentvariables" title="BuildEnvironmentVariables">BuildEnvironmentVariables</a>: <i>
      - <a href="buildenvironmentvariablesdefinition.md">BuildEnvironmentVariablesDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#entrypoint" title="EntryPoint">EntryPoint</a>: <i>String</i>
    <a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>: <i>
      - <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a></i>
    <a href="#httpstriggerurl" title="HttpsTriggerUrl">HttpsTriggerUrl</a>: <i>String</i>
    <a href="#ingresssettings" title="IngressSettings">IngressSettings</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#maxinstances" title="MaxInstances">MaxInstances</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
    <a href="#serviceaccountemail" title="ServiceAccountEmail">ServiceAccountEmail</a>: <i>String</i>
    <a href="#sourcearchivebucket" title="SourceArchiveBucket">SourceArchiveBucket</a>: <i>String</i>
    <a href="#sourcearchiveobject" title="SourceArchiveObject">SourceArchiveObject</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#triggerhttp" title="TriggerHttp">TriggerHttp</a>: <i>Boolean</i>
    <a href="#vpcconnector" title="VpcConnector">VpcConnector</a>: <i>String</i>
    <a href="#vpcconnectoregresssettings" title="VpcConnectorEgressSettings">VpcConnectorEgressSettings</a>: <i>String</i>
    <a href="#eventtrigger" title="EventTrigger">EventTrigger</a>: <i>
      - <a href="eventtriggerdefinition.md">EventTriggerDefinition</a></i>
    <a href="#sourcerepository" title="SourceRepository">SourceRepository</a>: <i>
      - <a href="sourcerepositorydefinition.md">SourceRepositoryDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AvailableMemoryMb

Memory (in MB), available to the function. Default value is `256`. Possible values include `128`, `256`, `512`, `1024`, etc.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildEnvironmentVariables

A set of key/value environment variable pairs available during build time.

_Required_: No

_Type_: List of <a href="buildenvironmentvariablesdefinition.md">BuildEnvironmentVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the function.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntryPoint

Name of the function that will be executed when the Google Cloud Function is triggered.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariables

A set of key/value environment variable pairs to assign to the function.

_Required_: No

_Type_: List of <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsTriggerUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressSettings

String value that controls what traffic can reach the function. Allowed values are `ALLOW_ALL`, `ALLOW_INTERNAL_AND_GCLB` and `ALLOW_INTERNAL_ONLY`. Changes to this field will recreate the cloud function.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

A set of key/value label pairs to assign to the function. Label keys must follow the requirements at https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements.

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxInstances

The limit on the maximum number of function instances that may coexist at a given time.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A user-defined name of the function. Function names must be unique globally.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

The runtime in which the function is going to run.
Eg. `"nodejs10"`, `"nodejs12"`, `"nodejs14"`, `"python37"`, `"python38"`, `"python39"`, `"dotnet3"`, `"go113"`, `"java11"`, `"ruby27"`, etc. Check the [official doc](https://cloud.google.com/functions/docs/concepts/exec#runtimes) for the up-to-date list.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountEmail

If provided, the self-provided service account to run the function with.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceArchiveBucket

The GCS bucket containing the zip archive which contains the function.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceArchiveObject

The source archive object (file) in archive bucket.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerHttp

Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcConnector

The VPC Network Connector that this cloud function can connect to. It should be set up as fully-qualified URI. The format of this field is `projects/*/locations/*/connectors/*`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcConnectorEgressSettings

The egress settings for the connector, controlling what traffic is diverted through it. Allowed values are `ALL_TRAFFIC` and `PRIVATE_RANGES_ONLY`. Defaults to `PRIVATE_RANGES_ONLY`. If unset, this field preserves the previously set value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventTrigger

_Required_: No

_Type_: List of <a href="eventtriggerdefinition.md">EventTriggerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceRepository

_Required_: No

_Type_: List of <a href="sourcerepositorydefinition.md">SourceRepositoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

