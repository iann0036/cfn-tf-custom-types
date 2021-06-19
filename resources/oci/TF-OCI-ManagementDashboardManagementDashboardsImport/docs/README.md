# TF::OCI::ManagementDashboardManagementDashboardsImport

This resource provides the Management Dashboards Import resource in Oracle Cloud Infrastructure Management Dashboard service.

Imports an array of dashboards and their saved searches. Import is designed to work with exportDashboard. An example using Oracle Cloud Infrastructure CLI is 
    $oci management-dashboard dashboard export --query data --export-dashboard-id "{\"dashboardIds\":[\"ocid1.managementdashboard.oc1..dashboardId1\"]}"  > dashboards.json
    $oci management-dashboard dashboard import --from-json file://dashboards.json

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::ManagementDashboardManagementDashboardsImport",
    "Properties" : {
        "<a href="#importdetails" title="ImportDetails">ImportDetails</a>" : <i>String</i>,
        "<a href="#importdetailsfile" title="ImportDetailsFile">ImportDetailsFile</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::ManagementDashboardManagementDashboardsImport
Properties:
    <a href="#importdetails" title="ImportDetails">ImportDetails</a>: <i>String</i>
    <a href="#importdetailsfile" title="ImportDetailsFile">ImportDetailsFile</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ImportDetails

Array of Dashboards to import. The `import_details` is mandatory if `import_details_path` is not passed. Value should be stringified JSON of [ManagementDashboardImportDetails](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/managementdashboard/20200901/ManagementDashboardImportDetails/).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportDetailsFile

_Required_: No

_Type_: String

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

