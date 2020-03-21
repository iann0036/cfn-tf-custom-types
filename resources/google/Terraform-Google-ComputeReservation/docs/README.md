# Terraform::Google::ComputeReservation

Represents a reservation resource. A reservation ensures that capacity is
held in a specific zone even if the reserved VMs are not running.

Reservations apply only to Compute Engine, Cloud Dataproc, and Google
Kubernetes Engine VM usage.Reservations do not apply to `f1-micro` or
`g1-small` machine types, preemptible VMs, sole tenant nodes, or other
services not listed above
like Cloud SQL and Dataflow.


To get more information about Reservation, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/reservations)
* How-to Guides
    * [Reserving zonal resources](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=reservation_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeReservation",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#specificreservationrequired" title="SpecificReservationRequired">SpecificReservationRequired</a>" : <i>Boolean</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#specificreservation" title="SpecificReservation">SpecificReservation</a>" : <i>[ <a href="specificreservation.md">SpecificReservation</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#instanceproperties" title="InstanceProperties">InstanceProperties</a>" : <i>[ <a href="instanceproperties.md">InstanceProperties</a>, ... ]</i>,
        "<a href="#guestaccelerators" title="GuestAccelerators">GuestAccelerators</a>" : <i>[ <a href="guestaccelerators.md">GuestAccelerators</a>, ... ]</i>,
        "<a href="#localssds" title="LocalSsds">LocalSsds</a>" : <i>[ <a href="localssds.md">LocalSsds</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeReservation
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#specificreservationrequired" title="SpecificReservationRequired">SpecificReservationRequired</a>: <i>Boolean</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#specificreservation" title="SpecificReservation">SpecificReservation</a>: <i>
      - <a href="specificreservation.md">SpecificReservation</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#instanceproperties" title="InstanceProperties">InstanceProperties</a>: <i>
      - <a href="instanceproperties.md">InstanceProperties</a></i>
    <a href="#guestaccelerators" title="GuestAccelerators">GuestAccelerators</a>: <i>
      - <a href="guestaccelerators.md">GuestAccelerators</a></i>
    <a href="#localssds" title="LocalSsds">LocalSsds</a>: <i>
      - <a href="localssds.md">LocalSsds</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpecificReservationRequired

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpecificReservation

_Required_: No

_Type_: List of <a href="specificreservation.md">SpecificReservation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceProperties

_Required_: No

_Type_: List of <a href="instanceproperties.md">InstanceProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestAccelerators

_Required_: No

_Type_: List of <a href="guestaccelerators.md">GuestAccelerators</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSsds

_Required_: No

_Type_: List of <a href="localssds.md">LocalSsds</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Commitment

Returns the <code>Commitment</code> value.

#### CreationTimestamp

Returns the <code>CreationTimestamp</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

#### Status

Returns the <code>Status</code> value.

