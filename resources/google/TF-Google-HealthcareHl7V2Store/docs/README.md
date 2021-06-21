# TF::Google::HealthcareHl7V2Store

A Hl7V2Store is a datastore inside a Healthcare dataset that conforms to the FHIR (https://www.hl7.org/hl7V2/STU3/)
standard for Healthcare information exchange


To get more information about Hl7V2Store, see:

* [API documentation](https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores)
* How-to Guides
    * [Creating a HL7v2 Store](https://cloud.google.com/healthcare/docs/how-tos/hl7v2)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=healthcare_hl7_v2_store_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::HealthcareHl7V2Store",
    "Properties" : {
        "<a href="#dataset" title="Dataset">Dataset</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationconfig" title="NotificationConfig">NotificationConfig</a>" : <i>[ <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a>, ... ]</i>,
        "<a href="#notificationconfigs" title="NotificationConfigs">NotificationConfigs</a>" : <i>[ <a href="notificationconfigsdefinition.md">NotificationConfigsDefinition</a>, ... ]</i>,
        "<a href="#parserconfig" title="ParserConfig">ParserConfig</a>" : <i>[ <a href="parserconfigdefinition.md">ParserConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::HealthcareHl7V2Store
Properties:
    <a href="#dataset" title="Dataset">Dataset</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationconfig" title="NotificationConfig">NotificationConfig</a>: <i>
      - <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a></i>
    <a href="#notificationconfigs" title="NotificationConfigs">NotificationConfigs</a>: <i>
      - <a href="notificationconfigsdefinition.md">NotificationConfigsDefinition</a></i>
    <a href="#parserconfig" title="ParserConfig">ParserConfig</a>: <i>
      - <a href="parserconfigdefinition.md">ParserConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Dataset

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationConfig

_Required_: No

_Type_: List of <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationConfigs

_Required_: No

_Type_: List of <a href="notificationconfigsdefinition.md">NotificationConfigsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParserConfig

_Required_: No

_Type_: List of <a href="parserconfigdefinition.md">ParserConfigDefinition</a>

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

#### SelfLink

Returns the <code>SelfLink</code> value.
